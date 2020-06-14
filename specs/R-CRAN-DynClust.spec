%global packname  DynClust
%global packver   3.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.13
Release:          2%{?dist}
Summary:          Denoising and clustering for dynamical image sequence (2D or3D)+T

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-parallel 
Requires:         R-parallel 

%description
DynClust is a two-stage procedure for the denoising and clustering of
stack of noisy images acquired over time. Clustering only assumes that the
data contain an unknown but small number of dynamic features. The method
first denoises the signals using local spatial and full temporal
information. The clustering step uses the previous output to aggregate
voxels based on the knowledge of their spatial neighborhood. Both steps
use a single keytool based on the statistical comparison of the difference
of two signals with the null signal. No assumption is therefore required
on the shape of the signals. The data are assumed to be normally
distributed (or at least follow a symmetric distribution) with a known
constant variance. Working pixelwise, the method can be time-consuming
depending on the size of the data-array but harnesses the power of
multicore cpus.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
