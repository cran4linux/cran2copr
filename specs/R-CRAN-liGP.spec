%global __brp_check_rpaths %{nil}
%global packname  liGP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Locally Induced Gaussian Process Regression

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-hetGP 
BuildRequires:    R-CRAN-laGP 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-hetGP 
Requires:         R-CRAN-laGP 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Performs locally induced approximate GP regression for large computer
experiments and spatial datasets following Cole D.A., Christianson, R.,
Gramacy, R.B. (2021) Statistics and Computing, 31(3), 1-21,
<arXiv:2008.12857>. The approximation is based on small local designs
combined with a set of inducing points (latent design points) for
predictions at particular inputs. Parallelization is supported for
generating predictions over an immense out-of-sample testing set. Local
optimization of the inducing points design is provided based on
variance-based criteria. Inducing point template schemes, including
scaling of space-filling designs, are also provided.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
