%global packname  JoF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Modelling and Simulating Judgments of Frequency

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
In a typical experiment for the intuitive judgment of frequencies (JoF)
different stimuli with different frequencies are presented. The
participants consider these stimuli with a constant duration and give a
judgment of frequency. These judgments can be simulated by formal models:
PASS 1 and PASS 2 based on Sedlmeier (2002, ISBN:978-0198508632), MINERVA
2 baesd on Hintzman (1984) <doi:10.3758/BF03202365> and TODAM 2 based on
Murdock, Smith & Bai (2001) <doi:10.1006/jmps.2000.1339>. The package
provides an assessment of the frequency by determining the core aspects of
these four models (attention, decay, and presented frequency) that can be
compared to empirical results.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
