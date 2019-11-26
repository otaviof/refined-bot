package refinedbot

// Intent describes the intention, the input employed to execute all actions.
type Intent struct {
	Action  string // one of the pre-defined actions
	Subject string // ticket number or intent subject
}

const StartPokerAction = "StartPoker"
const ShowPokerResultAction = "ShowPokerResult"

var Actions = []string{
	StartPokerAction,
	ShowPokerResultAction,
}
