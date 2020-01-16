%global packname  gender
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          Predict Gender from Names Using Historical Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9
BuildRequires:    R-CRAN-dplyr >= 0.4.2
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9
Requires:         R-CRAN-dplyr >= 0.4.2
Requires:         R-utils 
Requires:         R-stats 

%description
Infers state-recorded gender categories from first names and dates of
birth using historical datasets. By using these datasets instead of lists
of male and female names, this package is able to more accurately infer
the gender of a name, and it is able to report the probability that a name
was male or female. GUIDELINES: This method must be used cautiously and
responsibly. Please be sure to see the guidelines and warnings about usage
in the 'README' or the package documentation.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
