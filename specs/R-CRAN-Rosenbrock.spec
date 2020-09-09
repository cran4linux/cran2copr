%global packname  Rosenbrock
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Rosenbrock-Type Densities for Markov Chain Monte Carlo (MCMC) Sampler Benchmarking

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
New Markov chain Monte Carlo (MCMC) samplers new to be thoroughly tested
and their performance accurately assessed. This requires densities that
offer challenging properties to the novel sampling algorithms. One such
popular problem is the Rosenbrock function. However, while its shape lends
itself well to a benchmark problem, no codified multivariate expansion of
the density exists. We have developed an extension to this class of
distributions and supplied densities and direct sampler functions to
assess the performance of novel MCMC algorithms. The functions are
introduced in "An n-dimensional Rosenbrock Distribution for MCMC Testing"
by Pagani, Wiegand and Nadarajah (2019) <arXiv:1903.09556>.

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
