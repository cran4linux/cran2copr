%global __brp_check_rpaths %{nil}
%global packname  yarrr
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          A Companion to the e-Book "YaRrr!: The Pirate's Guide to R"

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-circlize 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-circlize 

%description
Contains a mixture of functions and data sets referred to in the
introductory e-book "YaRrr!: The Pirate's Guide to R". The latest version
of the e-book is available for free at
<https://www.thepiratesguidetor.com>.

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
