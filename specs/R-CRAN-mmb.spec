%global __brp_check_rpaths %{nil}
%global packname  mmb
%global packver   0.13.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.3
Release:          1%{?dist}%{?buildtag}
Summary:          Arbitrary Dependency Mixed Multivariate Bayesian Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-datasets 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-Rdpack 
Requires:         R-datasets 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Supports Bayesian models with full and partial (hence arbitrary)
dependencies between random variables. Discrete and continuous variables
are supported, and conditional joint probabilities and probability
densities are estimated using Kernel Density Estimation (KDE). The full
general form, which implements an extension to Bayes' theorem, as well as
the simple form, which is just a Bayesian network, both support regression
through segmentation and KDE and estimation of probability or relative
likelihood of discrete or continuous target random variables. This package
also provides true statistical distance measures based on Bayesian models.
Furthermore, these measures can be facilitated on neighborhood searches,
and to estimate the similarity and distance between data points. Related
work is by Bayes (1763) <doi:10.1098/rstl.1763.0053> and by Scutari (2010)
<doi:10.18637/jss.v035.i03>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
