%global __brp_check_rpaths %{nil}
%global packname  extremeStat
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Extreme Value Statistics and Quantile Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lmomco >= 2.2.5
BuildRequires:    R-CRAN-berryFunctions >= 1.15.6
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-evir 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-fExtremes 
BuildRequires:    R-CRAN-extRemes 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-Renext 
Requires:         R-CRAN-lmomco >= 2.2.5
Requires:         R-CRAN-berryFunctions >= 1.15.6
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-evir 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-fExtremes 
Requires:         R-CRAN-extRemes 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-Renext 

%description
Code to fit, plot and compare several (extreme value) distribution
functions. Can also compute (truncated) distribution quantile estimates
and draw a plot with return periods on a linear scale.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
