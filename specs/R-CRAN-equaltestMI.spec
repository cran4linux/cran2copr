%global packname  equaltestMI
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          2%{?dist}
Summary:          Examine Measurement Invariance via Equivalence Testing andProjection Method

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lavaan 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions for examining measurement invariance via equivalence testing are
included in this package. The traditionally used RMSEA (Root Mean Square
Error of Approximation) cutoff values are adjusted based on simulation
results. In addition, a projection-based method is implemented to test the
equality of latent factor means across groups without assuming the
equality of intercepts. For more information, see Yuan, K. H., & Chan, W.
(2016) <doi:10.1037/met0000080>, Deng, L., & Yuan, K. H. (2016)
<doi:10.1007/s11336-015-9491-8>, and Jiang, G., Mai, Y., & Yuan, K. H.
(2017) < doi:10.3389/fpsyg.2017.01823>.

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
