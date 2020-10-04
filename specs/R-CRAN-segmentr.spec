%global packname  segmentr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Segment Data With Maximum Likelihood

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glue 

%description
Given a likelihood provided by the user, this package applies it to a
given matrix dataset in order to find change points in the data that
maximize the sum of the likelihoods of all the segments. This package
provides a handful of algorithms with different time complexities and
assumption compromises so the user is able to choose the best one for the
problem at hand. The implementation of the segmentation algorithms in this
package are based on the paper by Bruno M. de Castro, Florencia Leonardi
(2018) <arXiv:1501.01756>. The Berlin weather sample dataset was provided
by Deutscher Wetterdienst <https://dwd.de/>. You can find all the
references in the Acknowledgments section of this package's repository via
the URL below.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
