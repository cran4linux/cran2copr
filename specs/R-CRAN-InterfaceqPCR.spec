%global __brp_check_rpaths %{nil}
%global packname  InterfaceqPCR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          GUI to Analyse qPCR Results after PMA Treatment or not

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-plyr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Graphical User Interface allowing to determine the concentration in the
sample in CFU per mL or in number of copies per mL provided to qPCR
results after with or without PMA treatment. This package is simply to use
because no knowledge in R commands is necessary. A graphic represents the
standard curve, and a table containing the result for each sample is
created.

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
