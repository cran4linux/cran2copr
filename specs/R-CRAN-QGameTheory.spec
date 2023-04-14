%global __brp_check_rpaths %{nil}
%global packname  QGameTheory
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Quantum Game Theory Simulator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-R.utils 

%description
General purpose toolbox for simulating quantum versions of game theoretic
models (Flitney and Abbott 2002) <arXiv:quant-ph/0208069>. Quantum
(Nielsen and Chuang 2010, ISBN:978-1-107-00217-3) versions of models that
have been handled are: Penny Flip Game (David A. Meyer 1998)
<arXiv:quant-ph/9804010>, Prisoner's Dilemma (J. Orlin Grabbe 2005)
<arXiv:quant-ph/0506219>, Two Person Duel (Flitney and Abbott 2004)
<arXiv:quant-ph/0305058>, Battle of the Sexes (Nawaz and Toor 2004)
<arXiv:quant-ph/0110096>, Hawk and Dove Game (Nawaz and Toor 2010)
<arXiv:quant-ph/0108075>, Newcomb's Paradox (Piotrowski and Sladkowski
2002) <arXiv:quant-ph/0202074> and Monty Hall Problem (Flitney and Abbott
2002) <arXiv:quant-ph/0109035>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
