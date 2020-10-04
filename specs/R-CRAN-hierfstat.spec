%global packname  hierfstat
%global packver   0.5-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Tests of Hierarchical F-Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-gaston 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-methods 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-gaston 
Requires:         R-CRAN-gtools 
Requires:         R-methods 

%description
Estimates hierarchical F-statistics from haploid or diploid genetic data
with any numbers of levels in the hierarchy, following the algorithm of
Yang (Evolution(1998), 52:950). Tests via randomisations the significance
of each F and variance components, using the likelihood-ratio statistics G
(Goudet et al. (1996) <https://www.genetics.org/content/144/4/1933>).
Estimates genetic diversity statistics for haploid and diploid genetic
datasets in various formats, including inbreeding and coancestry
coefficients, and population specific F-statistics following Weir and
Goudet (2017) <https://www.genetics.org/content/206/4/2085>.

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
