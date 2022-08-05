%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

Name:             jags
Version:          4.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Just Another Gibbs Sampler

License:          GPLv2
URL:              http://mcmc-jags.sourceforge.net
Source0:          https://downloads.sourceforge.net/mcmc-jags/JAGS-%{version}.tar.gz

BuildRequires:    gcc-c++, gcc-gfortran, libtool-ltdl
BuildRequires:    %{blaslib}-devel

%description
JAGS (Just Another Gibbs Sampler) is a program for the analysis of
Bayesian statistical models using Markov Chain Monte Carlo (MCMC)
simulation.

JAGS is similar to the BUGS (Bayesian Inference using Gibbs Sampling)
program developed at the MRC Biostatistics Unit, Cambridge, and uses a
dialect of the BUGS language to describe Bayesian hierarchical models.

%package devel
Summary:          Development Files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}
Requires:         gcc-c++, gcc-gfortran

%description devel
Development files for %{name}.

%prep
%setup -q -n JAGS-%{version}
export F77=gfortran

%build
%configure \
  --with-blas=-l%{blaslib}%{blasvar} \
  --with-lapack=-l%{blaslib}%{blasvar}
%make_build

%install
%make_install
find %{buildroot} -name *.la -exec rm {} \;

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}-terminal
%{_libdir}/JAGS
%{_libdir}/lib%{name}.so.*
%{_libdir}/libjrmath.so.*
%{_mandir}/man1/%{name}.1*

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/JAGS
%{_libdir}/lib%{name}.so
%{_libdir}/libjrmath.so

%changelog
* Fri Aug 05 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.3.0-3
- Modernize spec

* Sun Oct 04 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.3.0-2
- Build against optimized BLAS

* Wed Aug 14 2019 Iñaki Úcar <iucar@fedoraproject.org> - 4.3.0-1
- Some cleaning

* Wed Nov 4 2015 Lars Vilhuber <virtualrdc@cornell.edu> 4.0.0
- Adapting to JAGS 4.0.0

* Thu Feb 5 2009 Lars Vilhuber <virtualrdc@cornell.edu> 1.0.3-2
- Adapted to openSUSE build service
- Adjusted for building on SUSE systems (different Requires and BuildRequires)

* Thu Jul 17 2008 Martyn Plummer <martyn_plummer@sourceforge.net> 1.0.3-1
- Built JAGS 1.0.3

* Tue May 20 2008 Martyn Plummer <martyn_plummer@sourceforge.net> 1.0.2-3
- Modified descriptions
- Built on Fedora 9.

* Mon May 19 2008 Martyn Plummer <martyn_plummer@sourceforge.net> 1.0.2-2
- Moved libjags.so and libjrmath.so into devel package
- Added blas-devel as build requirement

* Fri May 16 2008 Martyn Plummer <martyn_plummer@sourceforge.net> 1.0.2-1
- First attempt
