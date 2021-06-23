%global __brp_check_rpaths %{nil}
%global packname  trueskill
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation the TrueSkill algorithm in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
An implementation of the TrueSkill algorithm (Herbrich, R., Minka, T. and
Grapel, T) in R; a Bayesian skill rating system with inference by
approximate message passing on a factor graph. Used by Xbox to rank gamers
and identify appropriate matches.
http://research.microsoft.com/en-us/projects/trueskill/default.aspx
Current version allows for one player per team. Will update as time
permits.  Requires R version 3.0 as it is written with Reference Classes.
URL: https://github.com/bhoung/trueskill-in-r Acknowledgements to Doug
Zongker and Heungsub Lee for their python implementations of the algorithm
and for the liberal reuse of Doug's code comments (@dougz and @sublee on
github).

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
%doc %{rlibdir}/%{packname}/example.r
%{rlibdir}/%{packname}/INDEX
