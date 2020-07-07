%global packname  BetaBit
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          Mini Games from Adventures of Beta and Bit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-digest 

%description
Three games: proton, frequon and regression. Each one is a console-based
data-crunching game for younger and older data scientists. Act as a
data-hacker and find Slawomir Pietraszko's credentials to the Proton
server. In proton you have to solve four data-based puzzles to find the
login and password. There are many ways to solve these puzzles. You may
use loops, data filtering, ordering, aggregation or other tools. Only
basics knowledge of R is required to play the game, yet the more functions
you know, the more approaches you can try. In frequon you will help to
perform statistical cryptanalytic attack on a corpus of ciphered messages.
This time seven sub-tasks are pushing the bar much higher. Do you accept
the challenge? In regression you will test your modeling skills in a
series of eight sub-tasks. Try only if ANOVA is your close friend. It's a
part of Beta and Bit project. You will find more about the Beta and Bit
project at <http://betabit.wiki>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
