%global __brp_check_rpaths %{nil}
%global packname  KSPM
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Semi-Parametric Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-DEoptim 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-DEoptim 

%description
To fit the kernel semi-parametric model and its extensions. It allows
multiple kernels and unlimited interactions in the same model.
Coefficients are estimated by maximizing a penalized log-likelihood;
penalization terms and hyperparameters are estimated by minimizing
leave-one-out error. It includes predictions with confidence/prediction
intervals, statistical tests for the significance of each kernel, a
procedure for variable selection and graphical tools for diagnostics and
interpretation of covariate effects. Currently it is implemented for
continuous dependent variables. The package is based on the paper of Liu
et al. (2007), <doi:10.1111/j.1541-0420.2007.00799.x>.

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
