%global __brp_check_rpaths %{nil}
%global packname  FisherEM
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          The FisherEM Algorithm to Simultaneously Cluster and Visualize High-Dimensional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-plyr 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-elasticnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-plyr 

%description
The FisherEM algorithm, proposed by Bouveyron & Brunet (2012)
<doi:10.1007/s11222-011-9249-9>, is an efficient method for the clustering
of high-dimensional data. FisherEM models and clusters the data in a
discriminative and low-dimensional latent subspace. It also provides a
low-dimensional representation of the clustered data. A sparse version of
Fisher-EM algorithm is also provided.

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
