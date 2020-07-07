%global packname  plot3logit
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}
Summary:          Ternary Plots for Trinomial Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggtern >= 3.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-Ternary >= 1.0.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggtern >= 3.3.0
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-Ternary >= 1.0.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-forcats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
An implementation of the ternary plot for interpreting regression
coefficients of trinomial regression models, as proposed in Santi, Dickson
and Espa (2019) <doi:10.1080/00031305.2018.1442368>. Ternary plots can be
drawn using either 'ggtern' package (based on 'ggplot2') or 'Ternary'
package (based on standard graphics).

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
