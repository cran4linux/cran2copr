%global __brp_check_rpaths %{nil}
%global packname  learningr
%global packver   0.29.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.29.1
Release:          3%{?dist}%{?buildtag}
Summary:          Data and Functions to Accompany the Book "Learning R"

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-plyr 

%description
Crabs in the English channel, deer skulls, English monarchs, half-caste
Manga characters, Jamaican cities, Shakespeare's The Tempest, drugged up
cyclists and sexually transmitted diseases.

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
