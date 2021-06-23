%global __brp_check_rpaths %{nil}
%global packname  RPEClust
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Projection Ensemble Clustering Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clusteval 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-clue 
Requires:         R-CRAN-clusteval 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-clue 

%description
Implements the methodology proposed by Anderlucci, Fortunato and Montanari
(2019) <arXiv:1909.10832> for high-dimensional unsupervised
classification. The random projection ensemble clustering algorithm
applies a Gaussian Mixture Model to different random projections of the
high-dimensional data and selects a subset of solutions accordingly to the
Bayesian Information Criterion, computed here as discussed in Raftery and
Dean (2006) <doi:10.1198/016214506000000113>. The clustering results
obtained on the selected projections are then aggregated via consensus to
derive the final partition.

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
