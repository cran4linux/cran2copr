%global __brp_check_rpaths %{nil}
%global packname  weirs
%global packver   0.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.25
Release:          3%{?dist}%{?buildtag}
Summary:          A Hydraulics Package to Compute Open-Channel Flow over Weirs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Provides computational support for flow over weirs, such as sharp-crested,
broad-crested, and embankments. Initially, the package supports broad- and
sharp-crested weirs.

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
