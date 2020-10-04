%global packname  klic
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}%{?buildtag}
Summary:          Kernel Learning Integrative Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-coca 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-utils 
Requires:         R-Matrix 
Requires:         R-cluster 
Requires:         R-CRAN-coca 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-pheatmap 
Requires:         R-utils 

%description
Kernel Learning Integrative Clustering (KLIC) is an algorithm that allows
to combine multiple kernels, each representing a different measure of the
similarity between a set of observations. The contribution of each kernel
on the final clustering is weighted according to the amount of information
carried by it. As well as providing the functions required to perform the
kernel-based clustering, this package also allows the user to simply give
the data as input: the kernels are then built using consensus clustering.
Different strategies to choose the best number of clusters are also
available. For further details please see Cabassi and Kirk (2020)
<doi:10.1093/bioinformatics/btaa593>.

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
