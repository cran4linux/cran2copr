%global packname  iCAMP
%global packver   1.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Infer Community Assembly Mechanisms by Phylogenetic-Bin-Based Null Model Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats4 
Requires:         R-CRAN-vegan 
Requires:         R-parallel 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats4 

%description
To implement a general framework to quantitatively infer Community
Assembly Mechanisms by Phylogenetic-bin-based null model analysis,
abbreviated as 'iCAMP' (Ning et al 2020) <doi:10.1101/2020.02.22.960872>.
It can quantitatively assess the relative importance of different
community assembly processes, such as selection, dispersal, and drift, for
both communities and each phylogenetic group ('bin'). Each bin usually
consists of different taxa from a family or an order. The package also
provides functions to implement some other published methods, including
neutral taxa percentage (Burns et al 2016) <doi:10.1038/ismej.2015.142>
based on neutral theory model (Sloan et al 2006)
<doi:10.1111/j.1462-2920.2005.00956.x> and quantifying assembly processes
based on entire-community null models (Stegen et al 2013)
<doi:10.1038/ismej.2013.93>. It also includes some handy functions,
particularly for big datasets, such as phylogenetic and taxonomic null
model analysis at both community and bin levels, between-taxa niche
difference and phylogenetic distance calculation, phylogenetic signal test
within phylogenetic groups, midpoint root of big trees, etc.

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
