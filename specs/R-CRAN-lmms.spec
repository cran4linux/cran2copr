%global packname  lmms
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}
Summary:          Linear Mixed Effect Model Splines for Modelling and Analysis ofTime Course Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-lmeSplines 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-nlme 
Requires:         R-CRAN-lmeSplines 
Requires:         R-parallel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-gridExtra 

%description
Linear Mixed effect Model Splines ('lmms') implements linear mixed effect
model splines for modelling and differential expression for highly
dimensional data sets: investNoise() for quality control and filterNoise()
for removing non-informative trajectories; lmmSpline() to model time
course expression profiles and lmmsDE() performs differential expression
analysis to identify differential expression between groups, time and/or
group x time interaction.

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
