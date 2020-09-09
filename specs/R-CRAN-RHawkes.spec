%global packname  RHawkes
%global packver   0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Renewal Hawkes Process

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-IHSEP 
Requires:         R-CRAN-IHSEP 

%description
Simulate a renewal Hawkes (RHawkes) self-exciting process, with a given
immigrant hazard rate function and offspring density function. Calculate
the likelihood of a RHawkes process with given hazard rate function and
offspring density function for an (increasing) sequence of event times.
Calculate the Rosenblatt residuals of the event times. Predict future
event times based on observed event times up to a given time. For details
see Chen and Stindl (2017) <doi:10.1080/10618600.2017.1341324>.

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
