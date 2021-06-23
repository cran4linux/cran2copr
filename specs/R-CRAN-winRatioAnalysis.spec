%global __brp_check_rpaths %{nil}
%global packname  winRatioAnalysis
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Estimates the Win-Ratio as a Function of Time

License:          GNU Affero General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-pssm 
BuildRequires:    R-CRAN-MLEcens 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-JM 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-survival 
Requires:         R-nlme 
Requires:         R-CRAN-plyr 
Requires:         R-Matrix 
Requires:         R-CRAN-pssm 
Requires:         R-CRAN-MLEcens 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-JM 
Requires:         R-CRAN-mvtnorm 

%description
Fits a model to data separately for each treatment group and then
calculates the win-Ratio as a function of follow-up time.

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
