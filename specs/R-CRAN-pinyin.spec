%global __brp_check_rpaths %{nil}
%global packname  pinyin
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Convert Chinese Characters into Pinyin, Sijiao, Wubi or OtherCodes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-splitstackshape 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-splitstackshape 
Requires:         R-CRAN-data.table 

%description
Convert Chinese characters into Pinyin (the official romanization system
for Standard Chinese in mainland China, Malaysia, Singapore, and Taiwan.
See <https://en.wikipedia.org/wiki/Pinyin> for details), Sijiao (four or
five numerical digits per character. See
<https://en.wikipedia.org/wiki/Four-Corner_Method>.), Wubi (an input
method with five strokes. See <https://en.wikipedia.org/wiki/Wubi_method>)
or user-defined codes.

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
