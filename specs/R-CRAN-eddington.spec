%global __brp_check_rpaths %{nil}
%global packname  eddington
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Compute a Cyclist's Eddington Number

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Compute a cyclist's Eddington number, including efficiently computing
cumulative E over a vector. A cyclist's Eddington number
<https://en.wikipedia.org/wiki/Arthur_Eddington#Eddington_number_for_cycling>
is the maximum number satisfying the condition such that a cyclist has
ridden E miles or greater in E days. The algorithm in this package is an
improvement over the conventional approach because both summary statistics
and cumulative statistics can be computed in linear time, since it does
not require initial sorting of the data. These functions may also be used
for computing h-indices for authors, a metric described by Hirsch (2005)
<doi:10.1073/pnas.0507655102>. Both are specific applications of computing
the side length of a Durfee square
<https://en.wikipedia.org/wiki/Durfee_square>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
