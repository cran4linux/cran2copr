%global __brp_check_rpaths %{nil}
%global packname  joinXL
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Perform Joins or Minus Queries on 'Excel' Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-timeSeries >= 3022.101
BuildRequires:    R-graphics >= 3.3.1
BuildRequires:    R-grDevices >= 3.3.1
BuildRequires:    R-stats >= 3.3.1
BuildRequires:    R-CRAN-openxlsx >= 3.0.0
BuildRequires:    R-CRAN-timeDate >= 2150
BuildRequires:    R-CRAN-R.utils >= 2.3.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-rChoiceDialogs >= 1.0.6
BuildRequires:    R-CRAN-rJava >= 0.9.8
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-readxl >= 0.1.1
Requires:         R-CRAN-timeSeries >= 3022.101
Requires:         R-graphics >= 3.3.1
Requires:         R-grDevices >= 3.3.1
Requires:         R-stats >= 3.3.1
Requires:         R-CRAN-openxlsx >= 3.0.0
Requires:         R-CRAN-timeDate >= 2150
Requires:         R-CRAN-R.utils >= 2.3.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-rChoiceDialogs >= 1.0.6
Requires:         R-CRAN-rJava >= 0.9.8
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-readxl >= 0.1.1

%description
Performs Joins and Minus Queries on 'Excel' Files fulljoinXL() Merges all
rows of 2 'Excel' files based upon a common column in the files.
innerjoinXL() Merges all rows from base file and join file when the join
condition is met. leftjoinXL() Merges all rows from the base file, and all
rows from the join file if the join condition is met. rightjoinXL() Merges
all rows from the join file, and all rows from the base file if the join
condition is met. minusXL() Performs 2 operations source-minus-target and
target-minus-source If the files are identical all output files will be
empty. Choose two 'Excel' files via a dialog box, and then follow prompts
at the console to choose a base or source file and columns to merge or
minus on.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
