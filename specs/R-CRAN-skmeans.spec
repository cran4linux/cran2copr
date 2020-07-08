%global packname  skmeans
%global packver   0.2-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.12
Release:          1%{?dist}
Summary:          Spherical k-Means Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-clue >= 0.3.39
BuildRequires:    R-CRAN-slam >= 0.1.31
BuildRequires:    R-cluster 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-clue >= 0.3.39
Requires:         R-CRAN-slam >= 0.1.31
Requires:         R-cluster 
Requires:         R-stats 
Requires:         R-utils 

%description
Algorithms to compute spherical k-means partitions. Features several
methods, including a genetic and a fixed-point algorithm and an interface
to the CLUTO vcluster program.

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
