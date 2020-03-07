%global packname  episensr
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}
Summary:          Basic Sensitivity Analysis of Epidemiological Results

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-trapezoid 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-trapezoid 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape 
Requires:         R-boot 
Requires:         R-CRAN-magrittr 

%description
Basic sensitivity analysis of the observed relative risks adjusting for
unmeasured confounding and misclassification of the exposure/outcome, or
both. It follows the bias analysis methods and examples from the book by
Lash T.L, Fox M.P, and Fink A.K. "Applying Quantitative Bias Analysis to
Epidemiologic Data", ('Springer', 2009).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
