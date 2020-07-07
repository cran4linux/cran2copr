%global packname  OutlierDetection
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Outlier Detection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DDoutlier 
BuildRequires:    R-CRAN-depth 
BuildRequires:    R-CRAN-depthTools 
BuildRequires:    R-CRAN-ldbod 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DDoutlier 
Requires:         R-CRAN-depth 
Requires:         R-CRAN-depthTools 
Requires:         R-CRAN-ldbod 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-plotly 

%description
To detect outliers using different methods namely model based outlier
detection (Barnett, V. 1978 <https://www.jstor.org/stable/2347159>),
distance based outlier detection (Hautamaki, V., Karkkainen, I., and
Franti, P. 2004 <http://cs.uef.fi/~franti/papers.html>), dispersion based
outlier detection (Jin, W., Tung, A., and Han, J. 2001
<https://link.springer.com/chapter/10.1007/0-387-25465-X_7>), depth based
outlier detection (Johnson, T., Kwok, I., and Ng, R.T. 1998
<http://www.aaai.org/Library/KDD/1998/kdd98-038.php>) and density based
outlier detection (Ester, M., Kriegel, H.-P., Sander, J., and Xu, X. 1996
<https://dl.acm.org/citation.cfm?id=3001507>). This package provides
labelling of observations as outliers and outlierliness of each outlier.
For univariate, bivariate and trivariate data, visualization is also
provided.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
