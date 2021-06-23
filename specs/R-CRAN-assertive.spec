%global __brp_check_rpaths %{nil}
%global packname  assertive
%global packver   0.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Readable Check Functions to Ensure Code Integrity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertive.base >= 0.0.4
BuildRequires:    R-CRAN-assertive.properties >= 0.0.2
BuildRequires:    R-CRAN-assertive.types >= 0.0.2
BuildRequires:    R-CRAN-assertive.sets >= 0.0.2
BuildRequires:    R-CRAN-assertive.reflection >= 0.0.2
BuildRequires:    R-CRAN-assertive.numbers 
BuildRequires:    R-CRAN-assertive.strings 
BuildRequires:    R-CRAN-assertive.datetimes 
BuildRequires:    R-CRAN-assertive.files 
BuildRequires:    R-CRAN-assertive.matrices 
BuildRequires:    R-CRAN-assertive.models 
BuildRequires:    R-CRAN-assertive.data 
BuildRequires:    R-CRAN-assertive.data.uk 
BuildRequires:    R-CRAN-assertive.data.us 
BuildRequires:    R-CRAN-assertive.code 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-assertive.base >= 0.0.4
Requires:         R-CRAN-assertive.properties >= 0.0.2
Requires:         R-CRAN-assertive.types >= 0.0.2
Requires:         R-CRAN-assertive.sets >= 0.0.2
Requires:         R-CRAN-assertive.reflection >= 0.0.2
Requires:         R-CRAN-assertive.numbers 
Requires:         R-CRAN-assertive.strings 
Requires:         R-CRAN-assertive.datetimes 
Requires:         R-CRAN-assertive.files 
Requires:         R-CRAN-assertive.matrices 
Requires:         R-CRAN-assertive.models 
Requires:         R-CRAN-assertive.data 
Requires:         R-CRAN-assertive.data.uk 
Requires:         R-CRAN-assertive.data.us 
Requires:         R-CRAN-assertive.code 
Requires:         R-CRAN-knitr 

%description
Lots of predicates (is_* functions) to check the state of your variables,
and assertions (assert_* functions) to throw errors if they aren't in the
right form.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
