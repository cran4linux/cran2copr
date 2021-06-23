%global __brp_check_rpaths %{nil}
%global packname  bahc
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Filter Covariance and Correlation Matrices with Bootstrapped-Averaged Hierarchical Ansatz

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-matrixStats 

%description
A method to filter correlation and covariance matrices by averaging
bootstrapped filtered hierarchical clustering and boosting. See Ch.
Bongiorno and D. Challet, Covariance matrix filtering with bootstrapped
hierarchies (2020) <arXiv:2003.05807> and Ch. Bongiorno and D. Challet,
Reactive Global Minimum Variance Portfolios with k-BAHC covariance
cleaning (2020) <arXiv:2005.08703>.

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
