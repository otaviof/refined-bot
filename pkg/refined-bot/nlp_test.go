package refinedbot

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestNLPNew(t *testing.T) {
	n := NewNLP()

	intent, err := n.Parse(`lets poker XYZ-1234?`)

	assert.NoError(t, err)
	assert.NotNil(t, intent)
	assert.Equal(t, StartPokerAction, intent.Action)
}
