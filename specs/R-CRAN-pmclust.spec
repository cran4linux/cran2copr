%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pmclust
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Model-Based Clustering using Expectation-Gathering-Maximization Algorithm for Finite Mixture Gaussian Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-pbdMPI >= 0.4.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-pbdMPI >= 0.4.2
Requires:         R-methods 
Requires:         R-CRAN-MASS 

%description
Aims to utilize model-based clustering (unsupervised) for high dimensional
and ultra large data, especially in a distributed manner. The code employs
'pbdMPI' to perform a expectation-gathering-maximization algorithm for
finite mixture Gaussian models. The unstructured dispersion matrices are
assumed in the Gaussian models. The implementation is default in the
single program multiple data programming model. The code can be executed
through 'pbdMPI' and MPI' implementations such as 'OpenMPI' and 'MPICH'.
See the High Performance Statistical Computing website
<https://snoweye.github.io/hpsc/> for more information, documents and
examples.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
