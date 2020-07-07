%global packname  rkeops
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          2%{?dist}
Summary:          Kernel Operations on the GPU, with Autodiff, without MemoryOverflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cmake
Requires:         cmake
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-openssl >= 1.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-openssl >= 1.3
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
The 'KeOps' library lets you compute generic reductions of very large
arrays whose entries are given by a mathematical formula. It combines a
tiled reduction scheme with an automatic differentiation engine, and can
be used through 'R', 'Matlab', 'NumPy' or 'PyTorch' backends. It is
perfectly suited to the computation of Kernel dot products and the
associated gradients, even when the full kernel matrix does not fit into
the GPU memory.

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
