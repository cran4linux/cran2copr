%global __brp_check_rpaths %{nil}
%global packname  ibd
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Incomplete Block Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-car 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-multcomp 

%description
A collection of several utility functions related to binary incomplete
block designs. The package contains function to generate A- and
D-efficient binary incomplete block designs with given numbers of
treatments, number of blocks and block size. The package also contains
function to generate an incomplete block design with specified concurrence
matrix. There are functions to generate balanced treatment incomplete
block designs and incomplete block designs for test versus control
treatments comparisons with specified concurrence matrix. Package also
allows performing analysis of variance of data and computing estimated
marginal means of factors from experiments using a connected incomplete
block design. Tests of hypothesis of treatment contrasts in incomplete
block design set up is supported.

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
