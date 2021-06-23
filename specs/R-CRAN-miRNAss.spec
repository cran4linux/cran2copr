%global __brp_check_rpaths %{nil}
%global packname  miRNAss
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Genome-Wide Discovery of Pre-miRNAs with few Labeled Examples

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-CORElearn 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-CORElearn 
Requires:         R-CRAN-RSpectra 

%description
Machine learning method specifically designed for pre-miRNA prediction. It
takes advantage of unlabeled sequences to improve the prediction rates
even when there are just a few positive examples, when the negative
examples are unreliable or are not good representatives of its class.
Furthermore, the method can automatically search for negative examples if
the user is unable to provide them. MiRNAss can find a good boundary to
divide the pre-miRNAs from other groups of sequences; it automatically
optimizes the threshold that defines the classes boundaries, and thus, it
is robust to high class imbalance. Each step of the method is scalable and
can handle large volumes of data.

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
