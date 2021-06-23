%global __brp_check_rpaths %{nil}
%global packname  WLasso
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection for Highly Correlated Predictors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-genlasso 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-Matrix 
Requires:         R-CRAN-genlasso 
Requires:         R-CRAN-tibble 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 

%description
It proposes a novel variable selection approach taking into account the
correlations that may exist between the predictors of the design matrix in
a high-dimensional linear model. Our approach consists in rewriting the
initial high-dimensional linear model to remove the correlation between
the predictors and in applying the generalized Lasso criterion. For
further details we refer the reader to the paper <arXiv:2007.10768> (Zhu
et al., 2020).

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
