%global __brp_check_rpaths %{nil}
%global packname  spAddins
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Set of RStudio Addins

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 

%description
A set of RStudio addins that are designed to be used in combination with
user-defined RStudio keyboard shortcuts. These addins either: 1) insert
text at a cursor position (e.g. insert operators %>%, <<-, %$%, etc.), 2)
replace symbols in selected pieces of text (e.g., convert backslashes to
forward slashes which results in stings like "c:data" converted into
"c:/data/") or 3) enclose text with special symbols (e.g., converts "bold"
into "**bold**") which is convenient for editing R Markdown files.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
