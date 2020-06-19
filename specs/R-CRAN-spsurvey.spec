%global packname  spsurvey
%global packver   4.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.3
Release:          1%{?dist}
Summary:          Spatial Survey Design and Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-crossdes 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-foreign 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-crossdes 
Requires:         R-CRAN-deldir 
Requires:         R-foreign 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-rgeos 
Requires:         R-stats 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 

%description
These functions provide procedures for selecting sites for spatial surveys
using spatially balanced algorithms applied to discrete points, linear
networks, or polygons. The probability survey designs available include
independent random samples, stratified random samples, and unequal
probability random samples (categorical or probability proportional to
size).  Design-based estimation based on the results from surveys is
available for estimating totals, means, quantiles, CDFs, and linear
models. The analyses rely on package survey for most results.  Variance
estimation options include a local neighborhood variance estimator that is
appropriate for spatially-balanced survey designs.  A reference for the
survey design portion of the package is: D. L. Stevens, Jr. and A. R.
Olsen (2004), "Spatially-balanced sampling of natural resources.", Journal
of the American Statistical Association 99(465): 262-278,
<DOI:10.1198/016214504000000250>. Additional helpful references for this
package are A. R. Olsen, T. M. Kincaid, and Q. Payton (2012) and T. M.
Kincaid and A. R. Olsen (2012), both of which are chapters in the book
"Design and Analysis of Long-Term Ecological Monitoring Studies" (R. A.
Gitzen, J. J. Millspaugh, A. B. Cooper, and D. S. Licht (eds.), Cambridge
University Press, New York, <Online ISBN:9781139022422>).

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
