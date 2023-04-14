%global __brp_check_rpaths %{nil}
%global packname  mra
%global packver   2.16.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.16.11
Release:          3%{?dist}%{?buildtag}
Summary:          Mark-Recapture Analysis

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Accomplishes mark-recapture analysis with covariates. Models available
include the Cormack-Jolly-Seber open population (Cormack (1972)
<doi:10.2307/2556151>; Jolly (1965) <doi:10.2307/2333826>; Seber (1965)
<doi:10.2307/2333827>) and Huggin's (1989) <doi:10.2307/2336377> closed
population. Link functions include logit, sine, and hazard.  Model
selection, model averaging, plot, and simulation routines included. Open
population size by the Horvitz-Thompson (1959) <doi:10.2307/2280784>
estimator.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
