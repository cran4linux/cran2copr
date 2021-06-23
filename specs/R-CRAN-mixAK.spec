%global __brp_check_rpaths %{nil}
%global packname  mixAK
%global packver   5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.3
Release:          2%{?dist}%{?buildtag}
Summary:          Multivariate Normal Mixture Models and Mixtures of GeneralizedLinear Mixed Models Including Model Based Clustering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-CRAN-colorspace 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-mnormt 
Requires:         R-parallel 
Requires:         R-CRAN-coda 

%description
Contains a mixture of statistical methods including the MCMC methods to
analyze normal mixtures. Additionally, model based clustering methods are
implemented to perform classification based on (multivariate) longitudinal
(or otherwise correlated) data. The basis for such clustering is a mixture
of multivariate generalized linear mixed models.

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
