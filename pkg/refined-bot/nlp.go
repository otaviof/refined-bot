package refinedbot

import (
	"fmt"
	"strings"

	"gopkg.in/jdkato/prose.v2"
)

type NLP struct {
	model *prose.Model
}

// actionPatterns links together the action name with the expected pattern of tokens.
var actionPatterns = map[string][]string{
	StartPokerAction: []string{
		"NNS VBP CD .",
		"MD PRP VB NNP .",
	},
}

// buildModel returns a local model for NLP.
func buildModel() *prose.Model {
	return prose.ModelFromData(
		"pokering", prose.UsingEntities(
			[]prose.EntityContext{
				{Text: "poker", Spans: []prose.LabeledEntity{{Label: "VB"}}},
			},
		),
	)
}

// match by comparing informed tokens to pattern, the tags must be the same.
func (n *NLP) match(tokens []prose.Token, pattern string) bool {
	patternSlice := strings.Split(pattern, " ")
	if len(patternSlice) < len(tokens) {
		return false
	}

	for i, token := range tokens {
		if token.Tag != patternSlice[i] {
			return false
		}
	}
	return true
}

// patternMatch based on global patterns, running match function against them until match.
func (n *NLP) patternMatch(tokens []prose.Token) string {
	for action, patterns := range actionPatterns {
		for _, pattern := range patterns {
			if n.match(tokens, pattern) {
				return action
			}
		}
	}
	return ""
}

// Parse will parse an phrase and try to identify the intent. It can return error on creating a
// document instance, and on identifying intent.
func (n *NLP) Parse(phrase string) (*Intent, error) {
	doc, err := prose.NewDocument(phrase, prose.UsingModel(n.model))
	if err != nil {
		return nil, err
	}

	action := n.patternMatch(doc.Tokens())
	if action == "" {
		return nil, fmt.Errorf("unable to identify action")
	}
	return &Intent{Action: action, Subject: ""}, nil
}

// NewNLP instantiate a new NLP instance, loading the data model.
func NewNLP() *NLP {
	return &NLP{model: buildModel()}
}
