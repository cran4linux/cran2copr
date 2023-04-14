%global __brp_check_rpaths %{nil}
%global packname  RViennaCL
%global packver   1.7.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1.8
Release:          3%{?dist}%{?buildtag}
Summary:          'ViennaCL' C++ Header Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
'ViennaCL' is a free open-source linear algebra library for computations
on many-core architectures (GPUs, MIC) and multi-core CPUs. The library is
written in C++ and supports 'CUDA', 'OpenCL', and 'OpenMP' (including
switches at runtime). I have placed these libraries in this package as a
more efficient distribution system for CRAN. The idea is that you can
write a package that depends on the 'ViennaCL' library and yet you do not
need to distribute a copy of this code with your package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
