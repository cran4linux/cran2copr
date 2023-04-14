%global __brp_check_rpaths %{nil}
%global packname  GIFTr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          GIFT Questions Format Generator from Dataframes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-glue 

%description
A framework and functions to create 'MOODLE' quizzes. 'GIFTr' takes
dataframe of questions of four types: multiple choices, numerical, true or
false and short answer questions, and exports a text file formatted in
'MOODLE' GIFT format. You can prepare a spreadsheet in any software and
import it into R to generate any number of questions with 'HTML',
'markdown' and 'LaTeX' support.

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
