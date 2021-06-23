%global __brp_check_rpaths %{nil}
%global packname  SEAGLE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Scalable Exact Algorithm for Large-Scale Set-Based GxE Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-CompQuadForm 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-CompQuadForm 

%description
The explosion of biobank data offers immediate opportunities for
gene-environment (GxE) interaction studies of complex diseases because of
the large sample sizes and rich collection in genetic and non-genetic
information. However, the extremely large sample size also introduces new
computational challenges in GxE assessment, especially for set-based GxE
variance component (VC) tests, a widely used strategy to boost overall GxE
signals and to evaluate the joint GxE effect of multiple variants from a
biologically meaningful unit (e.g., gene). We present 'SEAGLE', a Scalable
Exact AlGorithm for Large-scale Set-based GxE tests, to permit GxE VC test
scalable to biobank data. 'SEAGLE' employs modern matrix computations to
achieve the same “exact” results as the original GxE VC tests, and does
not impose additional assumptions nor relies on approximations. 'SEAGLE'
can easily accommodate sample sizes in the order of 10^5, is implementable
on standard laptops, and does not require specialized equipment. The
accompanying manuscript for this package can be found at Chi, Ipsen,
Hsiao, Lin, Wang, Lee, Lu, and Tzeng. (2021+) <arXiv:2105.03228>.

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
