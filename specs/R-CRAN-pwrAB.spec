%global __brp_check_rpaths %{nil}
%global packname  pwrAB
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Power Analysis for AB Testing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Power analysis for AB testing. The calculations are based on the Welch's
unequal variances t-test, which is generally preferred over the Student's
t-test when sample sizes and variances of the two groups are unequal,
which is frequently the case in AB testing. In such situations, the
Student's t-test will give biased results due to using the pooled standard
deviation, unlike the Welch's t-test.

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
