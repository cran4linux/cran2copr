%global __brp_check_rpaths %{nil}
%global packname  riceware
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}%{?buildtag}
Summary:          A Diceware Passphrase Implementation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-random >= 0.2.4
Requires:         R-CRAN-random >= 0.2.4

%description
The Diceware method can be used to generate strong passphrases. In short,
you roll a 6-faced dice 5 times in a row, the number obtained is matched
against a dictionary of easily remembered words. By combining together 7
words thus generated, you obtain a password that is relatively easy to
remember, but would take several millions years (on average) for a
powerful computer to guess.

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
