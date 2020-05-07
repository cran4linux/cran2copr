%global packname  blocksdesign
%global packver   4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0
Release:          1%{?dist}
Summary:          Nested and Crossed Block Designs for Factorial and UnstructuredTreatment Sets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-PolynomF 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-PolynomF 

%description
Constructs D-optimal or near D-optimal treatment and block designs for
linear treatment models with crossed or nested block factors. The
treatment design can be any arbitrary linear model defined by a treatment
model formula and the block design can be any feasible combination of
crossed or nested block factors. The block design factors are optimized
sequentially and the levels of each successive block factor are optimized
within the levels of each preceding block factor. Crossed block designs
with non-singular interaction effects are optimized using a weighting
scheme that allows for differential weighting of first and second-order
block effects. Outputs include a table showing the allocation of
treatments to blocks and tables showing the achieved D-efficiency factors
for each block and treatment design.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
