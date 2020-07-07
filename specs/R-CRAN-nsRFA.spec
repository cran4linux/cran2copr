%global packname  nsRFA
%global packver   0.7-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.15
Release:          3%{?dist}
Summary:          Non-Supervised Regional Frequency Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
A collection of statistical tools for objective (non-supervised)
applications of the Regional Frequency Analysis methods in hydrology. The
package refers to the index-value method and, more precisely, helps the
hydrologist to: (1) regionalize the index-value; (2) form homogeneous
regions with similar growth curves; (3) fit distribution functions to the
empirical regional growth curves. Most of the methods are those described
in the Flood Estimation Handbook (Centre for Ecology & Hydrology, 1999,
ISBN:9781906698003). Homogeneity tests from Hosking and Wallis (1993)
<doi:10.1029/92WR01980> and Viglione et al. (2007)
<doi:10.1029/2006WR005095> are available.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
