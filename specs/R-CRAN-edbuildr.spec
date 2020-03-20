%global packname  edbuildr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Automated School District Data Download and Processing

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 

%description
Import the 'EdBuild' master dataset of school district finance, student
demographics, and community economic indicators for every school district
in the United States. The master dataset is built from the US Census,
Annual Survey of School System Finances (F33) and joins data from the
National Center for Education Statistics, Common Core of Data; the US
Census, Small Area Income and Poverty Estimates; and the US Census,
Education Demographic and Geographic Estimates. We apply 'EdBuild'
standard processing to the dataset and provide the option to select from
four different exclusion criteria - see the masterpull() help file for
more details. The master dataset is available for any school year
2013-2017 or longitudinally for 2013-2017. Additional functions in the
package use 'EdBuild' master data to analyze the difference between
neighboring school districts and create formatted excel tables of school
district data. For full details about 'EdBuild' data processing please see
'EdBuild' (2019)
<https://edbuild.org/content/dividing-lines/main/methodology>.

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
%{rlibdir}/%{packname}/INDEX
