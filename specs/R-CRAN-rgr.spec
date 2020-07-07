%global packname  rgr
%global packver   1.1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.15
Release:          3%{?dist}
Summary:          Applied Geochemistry EDA

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-fastICA 
Requires:         R-MASS 
Requires:         R-CRAN-fastICA 

%description
Geological Survey of Canada (GSC) functions for exploratory data analysis
with applied geochemical data, with special application to the estimation
of background ranges and identification of outliers, 'anomalies', to
support mineral exploration and environmental studies.  Additional
functions are provided to support analytical data QA/QC, ANOVA for
investigations of field sampling and analytical variability, and utility
tasks.  NOTE: function caplot() for concentration-area plots employs
package 'akima', however, 'akima' is only licensed for not-for-profit use.
Therefore, not-for-profit users of 'rgr' will have to independently make
package 'akima' available through library(....); and use of function
caplot() by for-profit users will fail.

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
%doc %{rlibdir}/%{packname}/rgr_func_list_1-1-15.pdf
%doc %{rlibdir}/%{packname}/rgr_Overview_1-1-15.pdf
%doc %{rlibdir}/%{packname}/What_is_in_rgr_1-1-15.pdf
%{rlibdir}/%{packname}/INDEX
